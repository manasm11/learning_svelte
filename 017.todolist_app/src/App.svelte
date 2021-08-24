<script>
	import Header from "./components/Header.svelte";
	import List from "./components/List.svelte";
</script>

<main>
	<Header />
	<List />
</main>

<style>
	main {
		width: 500px;
		background: #009579;
	}

	:global(main *) {
		font-family: sans-serif;
	}
</style>
