<script context="module">
	export async function load({ fetch, page: { params } }) {
		if (!Number(params.authorId)) return;
        const [resUser, resPosts] = await Promise.all([
            fetch(`https://jsonplaceholder.typicode.com/users/${params.authorId}`),
            fetch('https://jsonplaceholder.typicode.com/posts'),
        ])
		
		return {
			props: {
				user: await resUser.json(),
				posts: (await resPosts.json()).filter(p=>p.userId == params.authorId)
			}
		};
	}
</script>

<script>
import Post from "$lib/Post.svelte";

	export let user, posts;
</script>

<center>
	<h1>{user.name}</h1>
	<p>{user.company.catchPhrase}</p>
	<p>{user.email}</p>
</center>

{#each posts as post}
	<Post {post}/>
{/each}

