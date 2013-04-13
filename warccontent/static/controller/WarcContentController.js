Ext.define('warccontent.controller.WarcContentController', {
    extend: 'Ext.app.Controller',
    
	init: function() {
		
//		// init selector tree view
//		this.getView('LinkTree')
//            .create()
//            .renderTo(Ext.get("body"))
//            .show();
		
        this.control({
        });
    },
	views: [
		'LinkTree'
    ],
	models: [
		'Link'
	],
	stores: [
		'Links'
	]
});