from vizualization_utils.hook_utils import HookUtils


class InputOutputFeatureMapsExtractor:

    def __init__(self, model):
        self.module_input_feature_maps_map = None
        self.module_output_feature_maps_map = None
        self.model = model
        hook_utils = HookUtils()
        hook_utils.deep_hook_register(model, self.feature_maps_hook, 'forward')

    def extract(self, input_image):
        self.module_input_feature_maps_map = {}
        self.module_output_feature_maps_map = {}
        self.model.forward(input_image)

    def get_module_input_and_output_feature_maps_map(self):
        if self.module_input_feature_maps_map == None or self.module_output_feature_maps_map == None:
            raise ValueError()
        else:
            return self.module_input_feature_maps_map, self.module_output_feature_maps_map

    def feature_maps_hook(self, module, input, output):
        self.module_input_feature_maps_map[module] = input[0]
        self.module_output_feature_maps_map[module] = output
