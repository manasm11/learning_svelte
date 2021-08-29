<script>
	export let post;
</script>

<a sveltekit:prefetch href="/blog/{post.id}">
	<div class="card clickable">
		<h2>{post.title}</h2>
		<p>{post.body}</p>
	</div>
</a>

