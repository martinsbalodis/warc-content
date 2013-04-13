Ext.define('warccontent.view.Viewport', {
    extend: 'Ext.container.Viewport',
    layout: 'border',
    items: [
        {
            xtype:'linktree',
            region: 'center'
        }
    ]
});