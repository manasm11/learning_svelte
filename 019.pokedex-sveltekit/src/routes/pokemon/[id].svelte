<script context="module">
    export async function load({page}) {
        const id = page.params.id;
        const url = `https://pokeapi.co/api/v2/pokemon/${id}`;
        const res = await fetch(url);
        const pokemon = await res.json();
        return {props: {pokemon}}
    }
</script>

<script>
    import {capitalizeFirstLetter} from '$utilities/string'
    export let pokemon
</script>

<h1>{capitalizeFirstLetter(pokemon.name)}</h1>

<style>
    h1 {
        display: flex;
        justify-content: center;
    }
</style>