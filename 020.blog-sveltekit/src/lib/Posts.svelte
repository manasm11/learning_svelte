<script>
	import { paginate, LightPaginationNav } from 'svelte-paginate';
	import Post from '$lib/Post.svelte';
	export let posts = [];

	let currentPage = 1;
	let pageSize = 10;
	$: paginatedPosts = paginate({ items: posts, pageSize, currentPage });
</script>

<div>
	{#each paginatedPosts as post}
		<Post {post} />
	{/each}
</div>
<LightPaginationNav
	totalItems={posts.length}
	{pageSize}
	{currentPage}
	limit={1}
	showStepOptions={true}
	on:setPage={(e) => (currentPage = e.detail.page)}
/>
