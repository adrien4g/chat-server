<script>
    export let username = ""
    export let message = ""
    export let selfMsg = false
</script>

<div class="msgBox" class:selfMsg={selfMsg}>
    <div>
        <p id="userData">{username}</p>
        <p id="msg">{message}</p>
    </div>
</div> 

<style>
    .msgBox{
        animation: in 200ms;
        background-color: white;
        width: max-content;
        margin: 5px 10px;
        border-radius: 15px;
    }
    .selfMsg{
        align-self: flex-end;
    }
    #userData{
        opacity: 50%;
        padding: 0px 10px;
    }
    #msg{
        padding: 0px 10px;
    }
    @keyframes in{
        from {opacity: 0%;transform: translateY(20px);}
        to {opacity: 100%;transform: translateY(0px);}
    }
</style>