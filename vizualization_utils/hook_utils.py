

class HookUtils():
    def deep_hook_register(self, model, hook, mode = 'forward'):
        if len(model._modules) > 0:
            for module in model._modules:
                self.deep_hook_register(model._modules[module],hook)
        else:
            if mode == 'forward':
                model.register_forward_hook(hook)
            elif mode == 'backward':
                model.register_backward_hook(hook)
            else:
                raise ValueError('Wrong mode')
