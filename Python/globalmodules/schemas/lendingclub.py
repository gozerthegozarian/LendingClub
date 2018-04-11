import pandas as pd


class SchemaLendingClub(object):

        dictionary={'id': 1077501, 'member_id': 1296599, 'loan_amnt': 5000.0, 'funded_amnt': 5000.0, 'funded_amnt_inv': 4975.0,
            'term': ' 36 months', 'int_rate': 10.65, 'installment': 162.87, 'grade': 'B', 'sub_grade': 'B2',
            'emp_title': 'str', 'emp_length': '10+ years', 'home_ownership': 'RENT', 'annual_inc': 24000.0,
            'verification_status': 'Verified', 'issue_d': 'Dec-2011', 'loan_status': 'Fully Paid', 'pymnt_plan': 'n',
            'url': 'https', 'desc': 'str', 'purpose': 'credit_card', 'title': 'Computer', 'zip_code': '860xx', 'addr_state': 'AZ',
            'dti': 27.65, 'delinq_2yrs': 0.0, 'earliest_cr_line': 'Jan-1985', 'inq_last_6mths': 1.0,
            'mths_since_last_delinq': 'str', 'mths_since_last_record': 0, 'open_acc': 3.0, 'pub_rec': 0.0, 'revol_bal': 13648.0,
            'revol_util': 83.7, 'total_acc': 9.0, 'initial_list_status': 'f', 'out_prncp': 0.0, 'out_prncp_inv': 0.0, 'total_pymnt': 5861.07141425,
            'total_pymnt_inv': 5831.78, 'total_rec_prncp': 5000.0, 'total_rec_int': 861.07, 'total_rec_late_fee': 0.0, 'recoveries': 0.0,
            'collection_recovery_fee': 0.0, 'last_pymnt_d': 'Jan-2015', 'last_pymnt_amnt': 171.62, 'next_pymnt_d': 'datetime',
            'last_credit_pull_d': 'Jan-2016', 'collections_12_mths_ex_med': 0.0, 'mths_since_last_major_derog': 'str', 'policy_code': 1.0,
            'application_type': 'INDIVIDUAL', 'annual_inc_joint': 'str', 'dti_joint': 'str', 'verification_status_joint': 'str',
            'acc_now_delinq': 0.0, 'tot_coll_amt': 'str', 'tot_cur_bal': 'str', 'open_acc_6m': 'str', 'open_il_6m': 'str',
            'open_il_12m': 'str', 'open_il_24m': 'str', 'mths_since_rcnt_il': 'str', 'total_bal_il': 'str', 'il_util': 'str', 'open_rv_12m': 'str',
            'open_rv_24m': 'str', 'max_bal_bc': 'str', 'all_util': 'str', 'total_rev_hi_lim': 'str', 'inq_fi': 'str', 'total_cu_tl': 'str', 'inq_last_12m': 'str'}


        df = pd.DataFrame(dictionary, index=[1], columns=dictionary.keys())

        columnheaders = ["id", "member_id", "loan_amnt", "funded_amnt", "funded_amnt_inv", "term", "int_rate", "installment", "grade", "sub_grade",
                              "emp_title", "emp_length", "home_ownership", "annual_inc", "verification_status", "issue_d", "loan_status", "pymnt_plan",
                              "url", "desc", "purpose", "title", "zip_code", "addr_state", "dti", "delinq_2yrs", "earliest_cr_line", "inq_last_6mths",
                              "mths_since_last_delinq", "mths_since_last_record", "open_acc", "pub_rec", "revol_bal", "revol_util", "total_acc",
                              "initial_list_status", "out_prncp", "out_prncp_inv", "total_pymnt", "total_pymnt_inv", "total_rec_prncp", "total_rec_int",
                              "total_rec_late_fee", "recoveries", "collection_recovery_fee", "last_pymnt_d", "last_pymnt_amnt", "next_pymnt_d", "last_credit_pull_d",
                              "collections_12_mths_ex_med", "mths_since_last_major_derog", "policy_code", "application_type", "annual_inc_joint", "dti_joint",
                              "verification_status_joint", "acc_now_delinq", "tot_coll_amt", "tot_cur_bal", "open_acc_6m", "open_il_6m", "open_il_12m", "open_il_24m",
                              "mths_since_rcnt_il", "total_bal_il", "il_util", "open_rv_12m", "open_rv_24m", "max_bal_bc", "all_util", "total_rev_hi_lim", "inq_fi",
                              "total_cu_tl", "inq_last_12m"]

        def __init__(self):
            pass

