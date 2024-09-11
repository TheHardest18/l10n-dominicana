import logging
from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def create_l10n_latam_manual_document_number(env):
    """
    ADD l10n_latam_manual_document_number if not exist
    """

    _logger.info("Dropping ir_sequence deprecated columns")
    create_query = """
        ALTER TABLE account_move
        ADD column IF NOT EXISTS l10n_latam_manual_document_number
        BOOLEAN;
        """
    _logger.info(
        """
        CREATING FIELDS
        l10n_latam_manual_document_number   ---->   STORE=TRUE
        """
    )
    env.cr.execute(create_query)


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    create_l10n_latam_manual_document_number(env)
