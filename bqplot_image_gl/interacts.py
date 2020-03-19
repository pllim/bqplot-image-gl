from bqplot.interacts import BrushSelector
from traitlets import Float, Unicode, Dict

class BrushEllipseSelector(BrushSelector):

    """BrushEllipse interval selector interaction.

    This 2-D selector interaction enables the user to select an ellipse
    region using the brushing action of the mouse. A mouse-down marks the
    center of the ellipse. The drag after the mouse down selects a point
    on the ellipse, drawn with the same aspect ratio as the change in x and y
    as measured in pixels. If pixel_aspect is set, the aspect ratio of the ellipse
    will be used instead. Note that the aspect ratio is respected in the view
    where the ellipse is drawn.

    Once an ellipse is drawn, it can be moved dragging, or reshaped by dragging
    the border.

    The selected_x and selected_y arrays define the bounding box of the ellipse.

    Attributes
    ----------
    selected_x: numpy.ndarray
        Two element array containing the start and end of the interval selected
        in terms of the x_scale of the selector.
        This attribute changes while the selection is being made with the
        ``BrushSelector``.
    selected_y: numpy.ndarray
        Two element array containing the start and end of the interval selected
        in terms of the y_scale of the selector.
        This attribute changes while the selection is being made with the
        ``BrushEllipseSelector``.
    brushing: bool (default: False)
        boolean attribute to indicate if the selector is being dragged.
        It is True when the selector is being moved and False when it is not.
        This attribute can be used to trigger computationally intensive code
        which should be run only on the interval selection being completed as
        opposed to code which should be run whenever selected is changing.
    """
    _view_module = Unicode('bqplot-image-gl').tag(sync=True)
    _model_module = Unicode('bqplot-image-gl').tag(sync=True)
    _view_module_version = Unicode('^0.2.0').tag(sync=True)
    _model_module_version = Unicode('^0.2.0').tag(sync=True)
    pixel_aspect = Float(None, allow_none=True).tag(sync=True)
    style = Dict({"fill": "green", "opacity": 0.3, "cursor": "grab"}).tag(sync=True)
    border_style = Dict({"stroke": "green", "fill": "none", "stroke-width": "3px",
                         "opacity": 0.3, "cursor": "col-resize"}).tag(sync=True)
    _view_name = Unicode('BrushEllipseSelector').tag(sync=True)
    _model_name = Unicode('BrushEllipseSelectorModel').tag(sync=True)