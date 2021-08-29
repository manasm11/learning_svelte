<script context="module">
	export async function load({ page }) {
		const id = page.params.id;
		const url = `https://pokeapi.co/api/v2/pokemon/${id}`;
		const res = await fetch(url);
		const pokemon = await res.json();
		return { props: { pokemon } };
	}
</script>

<script>
	import { capitalizeFirstLetter } from '$utilities/string';
	export let pokemon = {};
	const type = pokemon.types[0].type.name;
</script>

<center>
	<h1>{capitalizeFirstLetter(pokemon.name)}</h1>
	<img draggable="false" loading="lazy" src={pokemon.sprites['front_default']} alt={pokemon.name} />
	<p>type: <b>{capitalizeFirstLetter(type)}</b></p>
	<p>height: <b>{pokemon.height}</b></p>
	<p>weight: <b>{pokemon.weight}</b></p>
    <a sveltekit:prefetch href="/"><button>Back</button></a>
</center>

<style>
    h1 {
        text-decoration: underline;
		font-family: sans-serif;
    }
	p {
		font-size: 1.5rem;
        color: #222;
		font-family: monospace;
	}
</style>
