<script>
	import Node from "./Node.svelte";

	let directory_structure = {
		root: [
			{ dir1: [{ subdir11: [{ subsubdir1: [] }, { subdir12: [] }] }] },
			{ dir2: [{ subdir21: [] }] },
		],
	};
</script>

<h1>HELLO</h1>
{#each directory_structure.root as member}
	<Node {member} />
{/each}
