<script context="module">
	export async function load({ fetch }) {
		const res = await fetch('https://jsonplaceholder.typicode.com/posts');
		const data = await res.json();
		return {
			props: {
				posts: data
			}
		};
	}
</script>

<script>
	import Posts from '$lib/Posts.svelte';
	export let posts;
</script>

<center><h1>Posts</h1></center>
<Posts {posts} />
