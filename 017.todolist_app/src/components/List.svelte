<script>
    import { onMount } from "svelte";
    import items from "../stores/items.store";
    import Item from "./Item.svelte";
    import NewItem from './NewItem.svelte'

    function handleNewItem(e) {}

    onMount(async () => {
        await items.updateFromAPI();
    });
</script>

<div>
    <NewItem on:newitem={e=>items.addItem(e.detail.text)}/>
    {#each $items && items.sorted() as item (item.id)}
        <Item
            id={item.id}
            text={item.text}
            completed={item.completed}
            on:update={(e) => items.updateItem(e.detail)}
            on:delete={(e) => items.deleteItem(e.detail)}
        />
    {:else}
        <p>NO ITEMS EXIST</p>
    {/each}
</div>

<style>
    div {
        padding: 15px;
    }

    p {
        margin: 0;
        text-align: center;
        color: #ffffff;
        font-weight: bold;
        font-size: 1.1em;
    }
</style>
