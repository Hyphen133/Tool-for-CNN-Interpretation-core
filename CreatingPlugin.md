<h1>How to create own plugin?</h1>

In the CNN Visualization Tool there are 2 main categories of plugins. 
<p>
First of them is the one that is connected with graph nodes (like for example feature maps) 
or connected to some number of nodes (for example filters which are for convolutional layers).
The other category is for additional visualization that are not connected to specific nodes.

</p>
<br>

<h2>How to create GraphVisualization Plugin</h2>

<ol>
<li>Extend graph <code>GraphVisualizationTechnique</code> 
    <p>
    <pre>class MyPlugin(GraphVisualizationTechnique):
        ...</pre>
    </p>
</li> Specify <code>PrintingMode</code> (by defaults its normal)
    <p>
    <pre>def get_printing_mode(self):
        return PrintingMode.HEAPMAP</pre>
    </p>
</li>
</li> Override method <code>get_module_visualizations_list_map</code> to return maps in format {module:[list of 3d tensor maps]}
    <p>
    <pre>    def get_module_visualizations_list_map(self, model, image_tensor, class_index_vector):
        ...
        return module_maps_list_map</pre>
    </p>
    <p>
    Keep in mind that you do not have to specify visualizations for each module
    </p>
</li>

</li>   Enjoy your visualizations !!!
    
</li>
</ol>

<br>

<h2>How to create NonGraphVisualization Plugin</h2>

<ol>
<li>Extend graph <code>NonGraphVisualizationTechnique</code> 
    <p>
    <pre>class MyPlugin(NonGraphVisualizationTechnique):
        ...</pre>
    </p>
</li> Specify <code>PrintingMode</code> (by defaults its normal)
    <p>
    <pre>def get_printing_mode(self):
        return PrintingMode.HEAPMAP</pre>
    </p>
</li>
</li> Override method <code>get_additional_visualizations_maps</code> to return [list of 3d tensor maps]
    <p>
    <pre>    def get_additional_visualizations_maps(self, model, image_tensor, class_index_vector):
        return maps_list</pre>
    </p>
</li>

</li>   Enjoy your visualizations !!!
    
</li>
</ol>