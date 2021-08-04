<script>
	import Goodbye from "./Goodbye.svelte";
	const name = "Bro";
	const channel = "<h3>MyChannel izzzz OSSUM!!!</h3>";
	const id = "headingId";
	const disabled = true;
	const success = true;
</script>

<main>
	<h2 class="underlined">Undelined H2</h2>
	<h1 {id}>Hello {name}!</h1>
	<div class:success>{@html channel}</div>
	<button {disabled}>BUTTON 1 !!!</button>
	<button>Change Color</button>
	<Goodbye someName="Bruther !!!"/>
</main>

<style>
	.underlined {
		text-decoration: underline;
	}

	.success {
		color: olivedrab;
	}

	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
