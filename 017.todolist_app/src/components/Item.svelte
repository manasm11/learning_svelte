<script>
    import { createEventDispatcher } from "svelte";
    export let id, text, completed;
    const dispatch = createEventDispatcher();
</script>

<div
    class:completed
    on:dblclick={() => confirm("Delete ?") && dispatch("delete", id)}
>
    <input
        type="text"
        bind:value={text}
        readonly={completed}
        on:keydown={(e) => e.key === "Enter" && e.target.blur()}
        on:blur={() => dispatch("update", { id, completed, text })}
    />
    <input
        type="checkbox"
        bind:checked={completed}
        on:change={() => dispatch("update", { id, text, completed })}
    />
</div>

<style>
    div {
        display: flex;
        align-items: center;
        padding: 15px;
        background: #fff;
    }

    div:focus-within {
        background: rgba(255, 255, 255, 0.8);
    }

    input[type="text"] {
        flex-grow: 1;
        background: none;
        border: none;
        outline: none;
        font-weight: 500;
        font-size: 1rem;
    }

    input[type="checkbox"] {
        margin-left: 15px;
    }

    .completed {
        background: #ddd;
    }

    .completed input[type="text"] {
        color: #555;
        text-decoration: line-through;
    }
</style>
