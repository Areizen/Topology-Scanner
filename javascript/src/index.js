function main(container)
{
  // Checks if the browser is supported
  if (!mxClient.isBrowserSupported())
  {
    // Displays an error message if the browser is not supported.
    mxUtils.error('Browser is not supported!', 200, false);
  }else {
    var model = new mxGraphModel();
    var graph = new mxGraph(container, model);



    // Gets the default parent for inserting new cells. This
    // is normally the first child of the root (ie. layer 0).
    var parent = graph.getDefaultParent();

    // Adds cells to the model in a single step
    model.beginUpdate();
    try
    {

      x=100;
      y=100;

      width=200;
      height=30;

      $(xml).find('host').each(function (host) {
          ip = $(this).find("address").attr("addr")
          ports = $(this).find("port")
          label = ip+"\n"
          $(ports).each(function(port){
              label+="\n"+$(this).attr("protocol")+"\t"+$(this).attr("portid")+"\t"+$(this).find("service").attr("name")
          })

          parentVertex = graph.insertVertex(parent,null,label,x+(width+10)*host,y,width,height+$(ports).length*20)
      });
    }
    finally
    {
      // Updates the display
      model.endUpdate();
    }
  }
}
