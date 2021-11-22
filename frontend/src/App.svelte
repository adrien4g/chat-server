<script>
    import {sendMessage, socket} from './client.js'
    import MsgBox from './components/MsgBox.svelte'
    import ModalUsername from './components/ModalUsername.svelte'
    let messages = []

    socket.addEventListener('message', msg => {
        messages = [...messages, JSON.parse(msg.data)]
    })
    let msgBox = ""
    const onKeyPress = e => {
        if (e.charCode == 13) onSendMsg();
    }

    const onSendMsg = () =>{
        sendMessage(msgBox)
        messages = [...messages, {msg:msgBox, selfMsg:true, username: localStorage.getItem('username')}]
        msgBox = ""
    }

</script>
<main>
    {#if localStorage.getItem('username') == null}
    <ModalUsername />
    {/if}
    <div id="msgList">
        {#each messages as currentMsg}
            <MsgBox username={currentMsg.username} 
            message={currentMsg.msg} 
            selfMsg={currentMsg.selfMsg} />
        {/each}
    </div>
    <div id='inputDiv'>
        <input
            id="inputMsg"
            type="text"
            bind:value={msgBox}
            on:keypress={onKeyPress}
        />
        <button id="btnMsg" on:click={onSendMsg}>Enviar</button>
    </div>
</main>
<style>
    :global(body){
        padding: 0;
    }

    main{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: #ff7675;
    }
    main #msgList{
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        overflow: auto;
    }
    main #inputDiv{
        width: 100%;
        display: flex;
        align-self: flex-end;
    }
    main #inputDiv #inputMsg{
        width: 90%;
        margin: 15px;
    }
    main #inputDiv #btnMsg{
        flex: 1;
        margin: 15px 15px 15px 0px;
    }
</style>
