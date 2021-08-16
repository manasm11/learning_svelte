<script>
	import hobbies from "./hobbies.store";

	let gotUsname = false;
	let username = "";
	let hobbyInput;
	let loading = false;

	function loadData() {
		loading = true;
		hobbies.updateFromAPI(username).then(() => (loading = false));
	}

	function addHobby() {
		loading = true;
		hobbies.addHobby(hobbyInput.value, username).then(() => {
			hobbyInput.value = "";
			loading = false;
		});
	}

	function deleteHobby(id) {
		loading = true;
		hobbies.deleteHobby(id, username).then(() => (loading = false));
	}

	function login() {
		gotUsname = true
		loadData()
	}
</script>

{#if gotUsname}
	
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
{:else}
	<label>
		Enter username
		<input type="text" bind:value={username}>
	</label>
	<button on:click={login}>Login</button>
{/if}
