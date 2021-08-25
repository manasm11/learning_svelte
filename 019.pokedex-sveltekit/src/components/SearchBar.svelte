<script>
    export let search;
</script>

<div>
    <input type="text" bind:value={search} placeholder="Search Pokemon">
</div>

<style>
    div {
        display: flex;
        justify-content: center;
        margin-bottom: 2rem;
    }

    input:focus {
        outline: 1px black solid;
    }

    input {
        min-width: 300px;
    }
</style>