<script>
    import items from "../stores/items.store";
</script>

<header>
    <span>Dom's To-Do List</span>
    <span>{$items && items.completed()}/{$items && items.count()}</span>
</header>

<style>
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 20px;
        color: #ffffff;
        font-weight: bold;
        font-size: 1.5rem;
        background: rgba(0, 0, 0, 0.1);
    }
</style>
