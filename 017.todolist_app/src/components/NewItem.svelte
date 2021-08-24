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