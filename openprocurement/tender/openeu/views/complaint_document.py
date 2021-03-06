# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.tender.openua.views.complaint_document import TenderUaComplaintDocumentResource


@opresource(name='Tender EU Complaint Documents',
            collection_path='/tenders/{tender_id}/complaints/{complaint_id}/documents',
            path='/tenders/{tender_id}/complaints/{complaint_id}/documents/{document_id}',
            procurementMethodType='aboveThresholdEU',
            description="Tender complaint documents")
class TenderEUComplaintDocumentResource(TenderUaComplaintDocumentResource):
    pass
