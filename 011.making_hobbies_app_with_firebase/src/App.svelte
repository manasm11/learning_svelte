<script>
	import { onMount } from "svelte";

	import hobbies from "./hobbies.store";

	let hobbyInput;
	let loading = false;

	onMount(async () => {
		loading = true;
		hobbies.updateFromAPI().then(() => (loading = false));
	});

	function addHobby() {
		loading = true;
		hobbies.addHobby(hobbyInput.value).then(() => {
			hobbyInput.value = "";
			loading = false;
		});
	}

	function deleteHobby(id) {
		loading = true;
		hobbies.deleteHobby(id).then(() => (loading = false));
	}
</script>

<input type="text" bind:this={hobbyInput} />
<button on:click={addHobby}>Add Hobby</button>
<div>
	{#if loading}
		Loading...
	{:else}
		<ul>
			{#each $hobbies as hobby (hobby.id)}
				<li on:click={deleteHobby.bind(this, hobby.id)}>
					{hobby.value}
				</li>
			{/each}
		</ul>
	{/if}
</div>
