from odoo import http
from odoo.http import request

class MigrationController(http.Controller):

    @http.route('/run_migration', type='http', auth='user', methods=['GET'])
    def run_migration(self, **kw):
        try:
            # Import your migration script
            from odoo.addons.l10n_do_accounting.migrations.v16_1.post_init_migrate_fields import migrate as migrate1
            from odoo.addons.l10n_do_accounting.migrations.v16_1_1.post_init_migrate_fields import migrate as migrate2
            from odoo.addons.l10n_do_accounting.migrations.v16_1_2.post_init_migrate_fields import migrate as migrate3
            # Run the migration script
            migrate1(request.cr, '16.0')
            migrate2(request.cr, '16.0')
            migrate3(request.cr, '16.0')
            return "Migration completed successfully."
        except Exception as e:
            return f"An error occurred: {str(e)}"
