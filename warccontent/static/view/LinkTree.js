Ext.define('warccontent.view.LinkTree', {
    extend: 'Ext.tree.Panel',
    xtype: 'tree-grid',
    title: 'Warc content browser',
    alias: 'widget.linktree',
    height: 300,
    useArrows: true,
    rootVisible: false,
    multiSelect: true,
    singleExpand: true,
    store: 'Links',
    columns: [{
        xtype: 'treecolumn',
        text: 'path',
        flex: 1,
        sortable: true,
        dataIndex: 'path'
    },{
        xtype: 'templatecolumn',
        text: 'url',
        flex: 2,
        dataIndex: 'url',
        sortable: false,
        tpl: Ext.create('Ext.XTemplate', '{url:this.formatLink}', {
            formatLink: function(v) {
                return '<a href="'+v+'" target="_blank">'+v+'</a>';
            }
        })
    },{
        text: 'child count',
        width:100,
        dataIndex: 'childcount',
        sortable: true
    }]
});

