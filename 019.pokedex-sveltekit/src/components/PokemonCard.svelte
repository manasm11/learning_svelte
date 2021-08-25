<script>
	export let pokemon;
</script>

<div>
	<a href={`pokemon/${pokemon.id}`}>
		<img src={pokemon.image} alt={pokemon.name} />
		<h2>{pokemon.id}. {pokemon.name}</h2>
	</a>
</div>

<style>
	div {
		display: flex;
		flex-direction: column;
        align-items: center;
        justify-content: space-around;
        width: 250px;
        border: #ccc solid 1px;
        margin: 5px;
        box-shadow: 1px 1px 5px #ccc;
        background-color: #f1f5e1;
	}

    h2 {
        margin-top: 0;
    }
</style>
