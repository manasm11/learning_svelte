<script>
	import Post from '$lib/Post.svelte';
	export let posts;
</script>

<div>
	{#each posts as post}
		<Post {post} />
	{/each}
</div>

