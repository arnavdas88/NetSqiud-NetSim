from .Protocol import PingProtocol, ListenProtocol, BlankProtocol

class Kernel:
    parent = None
    def __init__(self, parent):

        self.parent = parent
        self.SYS = {
            "exit": BlankProtocol,
            "": BlankProtocol,

            # Pre-defined Protocols
            "ping": PingProtocol,
            "listen": ListenProtocol,
        }
        pass

    def __call__(self, ):
        pass

    def break_stack(self, stack):
        command = stack[0]
        argument = stack[1:]
        args = [ arg for arg in argument if "=" not in arg ]
        kwargs = { arg.split('=')[0]:arg.split('=')[1] for arg in argument if "=" in arg }
        args = [ self.parent.node, self.parent.telnet_client ] + args
        return command, args, kwargs

    def execute(self, stack):
        if stack in ["", ' ']:
            return

        command, args, kwargs = self.break_stack(stack)
        print(command, args, kwargs)
        if command in self.SYS:
            try:
                protocol = self.SYS[command](*args, **kwargs)
                protocol.start()
            except Exception as ex:
                self.parent.telnet_client.listener_push(f'Protocol Error [{command}] : {str(ex)}.')
        else:
            self.parent.telnet_client.listener_push(f'Cannot find the protocol {command}.')
        return

    def run(self, command):
        self.execute( [ ex for ex in command.split(' ') if not ex == '' ] )
        return
