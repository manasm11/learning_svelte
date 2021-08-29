<script>
	export let pokemon;
</script>

<a sveltekit:prefetch href={`/pokemon/${pokemon.id}`}>
	<div>
		<center>
			<img src={pokemon.image} alt={pokemon.name} />
		</center>
		<h2>{pokemon.name}</h2>
	</div>
</a>

<style>
	div {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		width: 12rem;
		border: #ccc solid 1px;
		margin: 5px;
		box-shadow: 1px 1px 5px #ccc;
		background-color: #f1f5e1;
	}

	h2 {
		margin-top: 0;
		font-family: monospace;
	}

	img {
		margin: auto;
	}
</style>
