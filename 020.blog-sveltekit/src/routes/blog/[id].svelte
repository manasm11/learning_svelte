<script context="module">
	export async function load({ page: { params }, fetch }) {
		if (!Number(params.id)) return;
		const resPost = await fetch(`https://jsonplaceholder.typicode.com/posts/${params.id}`);
		const post = await resPost.json();
		const resUser = await fetch(`https://jsonplaceholder.typicode.com/users/${post.userId}`);
		const user = await resUser.json();

		return {
			props: {
				post,
				user
			}
		};
	}
</script>

<script>
	export let post, user;
</script>

<div class="card">
	<h1>{post.title}</h1>
	<p>{post.body}</p>
	<p>- Written by: <a href="/author/{user.id}"><b>{user.name}</b></a></p>
</div>
