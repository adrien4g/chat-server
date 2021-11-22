<script>
    export let username = ""
    let noderef
    const onSetUsername = () => {
        if (username != ""){
            localStorage.setItem('username', username)
            noderef.parentNode.removeChild(noderef)
        }
    }
</script>

<main bind:this={noderef}>
    <div id="background">
        <div id="modal">
            <p>Insira seu nome</p>
            <input type="text" bind:value={username}/>
            <button on:click={() => onSetUsername()}>Entrar</button>
        </div>
    </div>
</main>

<style>
    #background{
        position: absolute;
        background-color: rgba(0, 0, 0, 0.3);
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    #background #modal{
        background-color: white;
        display: flex;
        align-items: center;
        flex-direction: column;
        border-radius: 15px;
        padding: 20px;
    }

    #background #modal button{
        cursor: pointer;
    }
</style>