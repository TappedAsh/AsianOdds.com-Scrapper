import xlsxwriter
import xlwt
#DATA Should be written from row 5 

def create_workbook(filename):
    workbook = xlwt.Workbook(filename)
    
    return workbook 
def open_workbook(filename):
    workbook = xlsxwriter.Workbook(filename)
    return workbook
def write_worksheet(workbook):
    worksheet = workbook.add_worksheet()
    return worksheet

def write_summary(worksheet , event_summary , row_number):
    date = event_summary["DATE"]
    time = event_summary["TIME"]
    league = event_summary["LEAGUE"]
    home = event_summary["HOME"]
    away = event_summary["AWAY"]

    worksheet.write_string(row_number ,0,date)
    worksheet.write_string(row_number ,1,time)
    worksheet.write_string(row_number ,2, league)
    worksheet.write_string(row_number ,3, home)
    worksheet.write_string(row_number ,4, away)

def write_scores(worksheet , scores , row_number):
    ft_score1 = scores["FT"]["1"]
    ft_score2 = scores["FT"]["2"]
    ht_score1 = scores["HT"]["1"]
    ht_score2 = scores["HT"]["2"]

    try:
        worksheet.write_number(row_number ,5, float(ht_score1))
        worksheet.write_number(row_number ,6, float(ht_score2))
        worksheet.write_number(row_number ,7, float(ft_score1))
        worksheet.write_number(row_number ,8, float(ft_score2))
    except ValueError:
        worksheet.write_string(row_number ,5, ht_score1)
        worksheet.write_string(row_number ,6, ht_score2)
        worksheet.write_string(row_number ,7, ft_score1)
        worksheet.write_string(row_number ,8, ft_score2)
        pass
def write_current(worksheet , current_odds , row_number):
    ft_spread_1 = current_odds["SPREAD"]["1"]
    ft_spread_2 = current_odds["SPREAD"]["2"]
    ft_odds_1 = current_odds["ODDS"]["1"]
    ft_odds_2 = current_odds["ODDS"]["2"]

    worksheet.write_string(row_number ,9, ft_spread_1)
    worksheet.write_string(row_number ,10, ft_spread_2)
    worksheet.write_string(row_number ,11, ft_odds_1)
    worksheet.write_string(row_number ,12, ft_odds_2)
def write_open_odds(worksheet , open_odds , row_number):
    ft_spread_1 = open_odds["SPREAD"]["1"]
    ft_spread_2 = open_odds["SPREAD"]["2"]
    ft_odds_1 = open_odds["ODDS"]["1"]
    ft_odds_2 = open_odds["ODDS"]["2"]

    worksheet.write_string(row_number ,13, ft_spread_1)
    worksheet.write_string(row_number ,14, ft_spread_2)
    worksheet.write_string(row_number ,15, ft_odds_1)
    worksheet.write_string(row_number ,16, ft_odds_2)
def write_total(worksheet , total , row_number):
    current = total["CURRENT"]
    _open = total["OPEN"]
    worksheet.write_string(row_number ,17, current)
    worksheet.write_string(row_number ,18, _open)
def write_overunder(worksheet , over_under , row_number):
    curr_over = over_under["CURRENT"]["OVER"]
    curr_under = over_under["CURRENT"]["UNDER"]
    opn_over = over_under["OPEN"]["OVER"]
    opn_under = over_under["OPEN"]["UNDER"]

    worksheet.write_string(row_number ,19, curr_over)
    worksheet.write_string(row_number , 20 , curr_under)
    worksheet.write_string(row_number ,21, opn_over)
    worksheet.write_string(row_number ,22, opn_under)
def write_moneyline(worksheet , moneyline , row_number):
    curr_1 = moneyline["CURRENT"]["1"]
    curr_x = moneyline["CURRENT"]["X"]
    curr_2 = moneyline["CURRENT"]["2"]
    opn_1  = moneyline["OPEN"]["1"]
    opn_x  = moneyline["OPEN"]["X"]
    opn_2 = moneyline["OPEN"]["2"]

    
    worksheet.write_string(row_number ,23, curr_1)
    worksheet.write_string(row_number ,24, curr_x)
    worksheet.write_string(row_number ,25, curr_2)
    worksheet.write_string(row_number ,26, opn_1)
    worksheet.write_string(row_number ,27, opn_x)
    worksheet.write_string(row_number ,28, opn_2)
