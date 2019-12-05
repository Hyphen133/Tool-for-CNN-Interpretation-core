class VisualizationTechnique():

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    # Checks if loaded model can be put into this technique
    # By convention model should be pretrained and ready for the visualization task
    def is_applicable_for(self, model):
        return True


class GraphVisualizationTechnique(VisualizationTechnique):
    def __init__(self, name) -> None:
        super().__init__(name)

    # Visualizations which can be connected with graph nodes
    def get_module_visualizations_list_map(self, model):
        pass


class NonGraphVisualizationTechnique(VisualizationTechnique):
    def __init__(self, name) -> None:
        super().__init__(name)

    # Visulaizations not connected with graph nodes
    def get_additional_visualizations_maps(self, model):
        pass
