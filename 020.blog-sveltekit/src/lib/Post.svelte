<script>
	export let post;
</script>

<a sveltekit:prefetch href="/blog/{post.id}">
	<div>
		<h2>{post.title}</h2>
		<p>{post.body}</p>
	</div>
</a>

<style>
	div {
		border: 1px solid #ccc;
		padding: 2rem;
		box-shadow: 2px 2px 10px #ccc;
		margin-bottom: 1rem;
		cursor: pointer;
		background-color: #fff;
	}

	div:hover {
		background-color: #f1f1f1;
	}

	div:active {
		box-shadow: 0.5px 0.5px 1px #ccc;
	}
</style>
