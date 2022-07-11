class Block:
    def __init__(self, name: str):
        self.id = block_id_from_name(name)

def block_id_from_name(name: str):
    match name:
        case 'air':
            return 0
        case 'grass':
            return 1
        case 'dirt':
            return 2
        case 'stone':
            return 3