<script>
	import Login from "./Login.svelte";
	import Feed from './Feed.svelte'

	const cmps = {
		login: {
			comp: Login,
			props: {
				"on:click": ()=>console.log("LOGGED IN")
			}
		},
		feed: {

		}
	};

	let name = "login";
</script>

<svelte:component this={cmps[name].comp} {...cmps[name].props} />
