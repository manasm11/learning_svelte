<script>
    export let member;

    let name = Object.keys(member)[0];
</script>

<h1>{name}</h1>
<ul>
    {#each member[name] as m}
        <li><svelte:self member={m} /></li>
    {/each}
</ul>

<style>
    li {
        margin-left: 2rem;
    }
</style>