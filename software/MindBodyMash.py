import pandas as pd
import glob
import sys, os
import numpy as np
import datetime


def MBfix(path_to_files=os.getcwd(), key='MBSystemID', **kwargs):

    path = path_to_files + '/*.csv'
    files = glob.glob(path)

    main = pd.DataFrame()

    for i in files:

        if "Clients" in i:
            con = pd.read_csv(i, index_col=None, dtype=object)

        if "Notes" in i:
            notes = pd.read_csv(i, index_col=None, dtype=object)

        if "CreditCards" in i:
            fin = pd.read_csv(i, index_col=None, dtype=object)

        if "ClientRelationships" in i:
            rel = pd.read_csv(i, index_col=None, dtype=object)

        if "ClientAutopayContract" in i:
            mem = pd.read_csv(i, index_col=None, dtype=object)

        if "ClientPricingOption" in i:
            mem2 = pd.read_csv(i, index_col=None, dtype=object)


    # Need to implement Custom Fields file import (orignal transfer didn't require)


    # Drop columns we can't use

    con.drop(['SpiritName', 'Dear', 'ForeignZip', 'Pager', 'FaxNumber',
     'CurrentSeries', 'BrochRequest', 'Parent', 'Location',
     'LoginName', 'Password', 'FirstClass', 'IPaddress','wspending', 'VerificationInfo',
     'SecretWord','SecretClue','SendMeReminders','Deleted','LiabilityRelease','LiabilityAgreementDate',
     'TrainerID', 'IsCompany','ExpectedIncome', 'Suspended', 'SuspendToDate','ShipAddress',
     'ShipPostalCode', 'SuspendFromDate','FirstContactDate','CloseDate','ExpectedCloseDate',
     'CloseProbability','RepID','BakCloseDate', 'RepID2','RepID3','OnlineSignUp','ShipCity','ShipState',
     'XRegionCopy','FirstClassDate','FirstApptDate','RepID4','RepID5','RepID6','ProspectStage',
     'InsuranceCompany','InsurancePolicyNum', 'CCExpireEmailSent','RefusedEmail','CloseEmailSent',
     'CloseFollowupEmailSent','ApptGenderPrefMale','MobileProvider','AutomatedContactMethod',
     'AllowMissingBillingAlert','Is3rdParty','CreatedBy', 'DeactivatedTime','StatusID','ShipCountry',
     'RewardsOptIn','AllowAccountPurchases','MergeTimeStamp','MergeEmpID','MergeClientID',
     'AccountPaymentsAllowed', 'AutoPayLimit', 'FirstVisitApptEmailSent','FirstVisitResEmailSent',
     'ReactivatedTime','LockerNo','IsSystem','MeasurementsTaken', 'LiabilityRelBy','LiabilityAgreementDate1',
     'ReferrerID','Longitude','Latitude','LockerDate','LastFormulaNotes','MBFVisitorID','ChangePassword',
     'ModifiedBy','Modified','PasswordChangeKey','EmailStatus','ConvertedDate', 'QBOID', 'HomeStudio'], axis=1, inplace=True)

    fin.drop(['BillingStreetAddress','BillingCity','BillingState','BillingZip','ccType', 'BarcodeID'], axis=1, inplace=True)

    rel.drop(['RelationID','BarcodeID1', 'BarcodeID2'], axis=1, inplace=True)

    mem.drop(['PayerBarcodeID','PayerLastName','PayerFirstName', 'TerminationDate',
    'RunDateTime', 'Contract Agreement Date', 'LocationName', 'AutoPayItemDescription'], axis=1, inplace=True)

    mem2.drop(['BarcodeID','Returned', 'Duration', 'DurationUnit', 'PaymentDataID', 'ItemType',
    'NumClasses', 'PaymentAmount', 'Program/Service Category', 'FirstName', 'LastName'], axis=1, inplace=True)



    # Clean Up

    mem['ScheduleDate'] = pd.to_datetime(mem['ScheduleDate'])


    # ------ Super slow solution -------- open to suggestions here

    new_mem = []

    for name, group in mem.groupby('MBSystemID'):

        # group is the member

        for subname, subgroup in group.groupby(['Contract Start Date','Contract End Date']):

            # subgroup is the membership payments 

            tempFuture = pd.DataFrame(columns=mem.columns.values)
            tempPast = pd.DataFrame(columns=mem.columns.values)

            for index, row in subgroup.iterrows():

                # row is the payment 

                if row['ScheduleDate'].date() > datetime.date.today():
                    tempFuture = tempFuture.append(row)

                elif row['ScheduleDate'].date() < datetime.date.today():
                    tempPast = tempPast.append(row)


            if len(tempFuture.index) != 0:

                mostRecent = tempFuture.sort_values('ScheduleDate', ascending=True).head(1).to_dict('list')
                new_mem.append(mostRecent)
                
            else:
                
                mostRecent = tempPast.sort_values('ScheduleDate', ascending=True).head(1).to_dict('list')
                new_mem.append(mostRecent)
                
        # lets you know the progress

        print('New Member -- ' + str(name) + '/' + str(mem['MBSystemID'].max()))
        print(type(new_mem[1]))

    mem = pd.DataFrame.from_dict(new_mem)


    # -------- End slow solution ---------

    mem['Amount'] = mem['Amount'].str.replace(r'00$', '')
    mem['PaymentMethod'] = mem['PaymentMethod'].str.replace('Credit Card', 'CC')
    mem['PaymentMethod'] = mem['PaymentMethod'].str.replace('ACH', 'EFT')
    mem['PaymentMethod'] = mem['PaymentMethod'].str.replace('Debit Account', 'CC')
    # mem = mem.str.replace({r'^[\'': '\']$', '')

    mem.rename(columns={'ContractName': 'Current Program'}, inplace=True)

    # If ContractDeleted = True, delete row

    # Replace Dates that we need to sort by with datetimes
    mem['Contract Start Date'] = pd.to_datetime(mem['Contract Start Date'])

    # Merge files

    #complete = pd.merge(con, mem, on=['Last Att. Date', 'Full Name'], how='left')

    # Output files

    try:
        os.mkdir('clean')
    except Exception:
        pass

    con.name = 'Contacts'
    mem.name = 'Memberships'
    mem2.name = 'Memberships 2'
    fin.name = 'Financials'
    rel.name = 'Relationships'
#    complete.name = 'Complete_File'

    for i in [con, mem, mem2, fin, rel]:

        i.to_csv('clean/' + i.name + '.csv', quoting=1, index=False)
