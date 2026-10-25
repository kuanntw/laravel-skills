# Template — HTTP 授權測試起手式

以下為本套件撰寫的 PHPUnit 範例，不是可直接在本 skills repository 執行的 application test。使用前依版本分流調整模型、factory、路由、guard、欄位、policy 與 test runner，禁止為了符合範例改正式 schema 或安裝新依賴。

## 範例契約
- 專案有 `Tenant`、`User`、`Order` factories；`User` 有 `tenant_id` / `role`，`Order` 有 `tenant_id` / `title`。
- `orders.update` 是受保護的 PUT JSON route；server 從登入會員建立 tenant context。若專案以 host / session 選 tenant，先用既有測試 helper 設定 A，再測竄改。
- 同租戶 editor 可更新，viewer 回 403；跨租戶 resource 回 404；成功回 200；空白 title 回 422。這只是此範例選定契約，不代表所有專案必須一樣。
- 業務 action 會 dispatch `App\Events\OrderUpdated`，接受 `orderId`；依專案實際事件替換。只 fake 此事件，讓 model / tenant observer 照常執行。
- 確認隔離測試 DB 後使用 `RefreshDatabase`。

```php
<?php

namespace Tests\Feature;

use App\Events\OrderUpdated;
use App\Models\Order;
use App\Models\Tenant;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Event;
use Tests\TestCase;

class OrderAuthorizationTest extends TestCase
{
    use RefreshDatabase;

    public function test_allowed_actor_updates_own_tenant_order(): void
    {
        $tenant = Tenant::factory()->create();
        $actor = User::factory()->create(['tenant_id' => $tenant->id, 'role' => 'editor']);
        $order = Order::factory()->create(['tenant_id' => $tenant->id, 'title' => '原標題']);
        Event::fake([OrderUpdated::class]);

        $this->actingAs($actor)->putJson(route('orders.update', $order), ['title' => '新標題'])
            ->assertOk();

        $this->assertDatabaseHas('orders', [
            'id' => $order->id, 'tenant_id' => $tenant->id, 'title' => '新標題',
        ]);
        Event::assertDispatched(OrderUpdated::class, 1);
        Event::assertDispatched(OrderUpdated::class, fn ($event) => $event->orderId === $order->id);
    }

    public function test_denied_actor_cannot_update_even_with_valid_payload(): void
    {
        $tenant = Tenant::factory()->create();
        $actor = User::factory()->create(['tenant_id' => $tenant->id, 'role' => 'viewer']);
        $order = Order::factory()->create(['tenant_id' => $tenant->id, 'title' => '原標題']);
        $before = $order->getAttributes();
        $count = Order::count();
        Event::fake([OrderUpdated::class]);

        $this->actingAs($actor)->putJson(route('orders.update', $order), ['title' => '新標題'])
            ->assertForbidden();

        $this->assertSame($before, $order->fresh()->getAttributes());
        $this->assertSame($count, Order::count());
        Event::assertNotDispatched(OrderUpdated::class);
    }

    public function test_cross_tenant_actor_cannot_update_even_with_valid_payload(): void
    {
        $tenantA = Tenant::factory()->create();
        $tenantB = Tenant::factory()->create();
        $actor = User::factory()->create(['tenant_id' => $tenantA->id, 'role' => 'editor']);
        $order = Order::factory()->create(['tenant_id' => $tenantB->id, 'title' => 'B 的標題']);
        // 以測試 DB 的直接快照確認 B 不變，避免 assertion 也被 A 的 global scope 過濾。
        $before = \Illuminate\Support\Facades\DB::table('orders')->where('id', $order->id)->first();
        $count = \Illuminate\Support\Facades\DB::table('orders')->count();
        Event::fake([OrderUpdated::class]);

        $response = $this->actingAs($actor)->putJson(route('orders.update', $order), ['title' => '新標題']);
        $response->assertNotFound();
        // 先解析 JSON 再檢查，避免 Unicode escape 讓原始 response 字串檢查漏掉洩漏。
        // JSON 不合法也必須使測試失敗；正規化後可檢出巢狀 error message 內的標題。
        $decoded = json_decode($response->getContent(), true, 512, JSON_THROW_ON_ERROR);
        $normalized = json_encode($decoded, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_THROW_ON_ERROR);
        $this->assertStringNotContainsString('B 的標題', $normalized);

        $this->assertEquals($before, \Illuminate\Support\Facades\DB::table('orders')->where('id', $order->id)->first());
        $this->assertSame($count, \Illuminate\Support\Facades\DB::table('orders')->count());
        Event::assertNotDispatched(OrderUpdated::class);
    }

    public function test_authorized_actor_still_needs_valid_input(): void
    {
        $tenant = Tenant::factory()->create();
        $actor = User::factory()->create(['tenant_id' => $tenant->id, 'role' => 'editor']);
        $order = Order::factory()->create(['tenant_id' => $tenant->id, 'title' => '原標題']);
        $before = $order->getAttributes();
        Event::fake([OrderUpdated::class]);

        $this->actingAs($actor)->putJson(route('orders.update', $order), ['title' => ''])
            ->assertUnprocessable()->assertJsonValidationErrors('title');

        $this->assertSame($before, $order->fresh()->getAttributes());
        Event::assertNotDispatched(OrderUpdated::class);
    }
}
```

## 接續擴充，不可停在四個案例
- 依 [安全驗收矩陣](security-acceptance-matrix.md) 複製到 create / delete / read / bulk / export / import；補 guest、B→A、nested relation、mass assignment 與 query allowlist。
- create / update 注入 `tenant_id`、`owner_id`、`role`、`is_admin` 時，固定拒絕或忽略契約，查 DB 比較敏感欄位，不能只 assert status。
- sort 以兩筆不同值驗證正確順序；非法 sort / filter 要測保護欄位、SQL 片段與外租戶 ID，確認不洩漏 records / totals。
- 若 action 直接 dispatch job / mail / notification / HTTP webhook，另使用專案既有 fake / spy 斷言未送出，不以「事件沒發」推定所有副作用都安全。
- Livewire 同樣用合法 payload 直接 `call('save')` / `call('delete', $foreignId)`，測 set 公開 ID / tenant / sort 欄位後仍被 server 拒絕；使用相同 major 的 assertion API。
- 驗證命令示例：`php artisan test --filter=OrderAuthorizationTest`，再跑專案完整 suite。未裝 PHP / vendor / 測試 DB 時標記「未執行」，不宣稱通過。
