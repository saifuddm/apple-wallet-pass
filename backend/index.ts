console.log("Hello via Bun!");

const server = Bun.serve({
    port: 3000,
    fetch(request: Request) {
        const url = new URL(request.url);
        console.log(`Server triggered for ${url.pathname}`);
        console.log(request)
        return new Response("Hello via Bun!");
    }
})

console.log(`Server started at http://${server.hostname}:${server.port}`);