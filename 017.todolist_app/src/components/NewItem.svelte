<script>
    import {createEventDispatcher} from 'svelte'
    const dispatch = createEventDispatcher();

    let value = ""

    function handleKeydown(e) {
        if(e.key !== "Enter" || value.length === 0) return;
        dispatch("newitem", {text: value})
        value = ""
    }
</script>

<input type="text" bind:value placeholder="+ ADD NEW ITEM" on:keydown={handleKeydown}/>

<style>
    input {
        box-sizing: border-box;
        margin-bottom: 15px;
        padding: 15px;
        border: none;
        outline: none;
        width: 100%;
        background: rgba(0, 0, 0, 0.25);
        color: #fff;
        font-weight: bold;
        cursor: pointer;
    }

    input::placeholder {
        color: #fff;
    }
</style>