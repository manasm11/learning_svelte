<script>
	import PokemonCard from '$components/PokemonCard.svelte';
	import SearchBar from '$components/SearchBar.svelte';
	import pokemons from '$stores/poke-stores';

	let search = '';

	$: filteredPokemons = $pokemons
		.filter((p) => p.name.toLowerCase().includes(search.toLowerCase()))
		.slice(0, 400);
</script>

<svelte:head><title>Pokedex</title></svelte:head>
<h1>Pokedex</h1>
<SearchBar bind:search />
<div>
	{#each filteredPokemons as pokemon (pokemon.name)}
		<PokemonCard {pokemon} />
	{/each}
</div>

<style>
	div {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: center;
	}

	h1 {
		display: flex;
		justify-content: center;
		font-size: 3rem;
		text-decoration: underline;
		font-family: sans-serif;
	}
</style>
