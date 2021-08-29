<script>
	import PokemonCard from '$components/PokemonCard.svelte';
	import SearchBar from '$components/SearchBar.svelte';
	import pokemons from '$stores/poke-stores';
	import { paginate, LightPaginationNav } from 'svelte-paginate';

	let search = '';
	let items = $pokemons.filter((p) => p.name.toLowerCase().includes(search.toLowerCase()));
	let currentPage = 1;
	let pageSize = 80;
	$: paginatedItems = paginate({
		items,
		pageSize,
		currentPage
	});
</script>

<svelte:head><title>Pokedex</title></svelte:head>
<h1>Pokedex</h1>
<SearchBar bind:search />
<div>
	{#each paginatedItems as pokemon (pokemon.name)}
		<PokemonCard {pokemon} />
	{/each}
</div>
<LightPaginationNav
	totalItems={items.length}
	{pageSize}
	{currentPage}
	limit={1}
	showStepOptions={true}
	on:setPage={(e) => (currentPage = e.detail.page)}
/>

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
