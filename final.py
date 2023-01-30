import json
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"

web3= Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

# abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rid","type":"uint256"},{"indexed":false,"internalType":"string","name":"rname","type":"string"}],"name":"addReportEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tid","type":"uint256"},{"indexed":false,"internalType":"string","name":"tName","type":"string"}],"name":"addTaskEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"avgRating","type":"uint256"}],"name":"reviewReportEvent","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"ReportIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"TaskIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalRating","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalTasks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalwSubmittedReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wAddress","type":"address"},{"internalType":"string","name":"rname","type":"string"},{"internalType":"string","name":"_content","type":"string"}],"name":"addReport","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"rAddress","type":"address"},{"internalType":"string","name":"tName","type":"string"},{"internalType":"string","name":"tDescription","type":"string"},{"internalType":"uint256","name":"minAmtForTask","type":"uint256"}],"name":"addTask","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllReportIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllTaskIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getAllWorkersForReport","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getCurrentWorkerComments","outputs":[{"internalType":"string","name":"wComments","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getCurrentWorkerRating","outputs":[{"internalType":"uint256","name":"wRating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getReport","outputs":[{"components":[{"internalType":"string","name":"reportName","type":"string"},{"internalType":"string","name":"reportContent","type":"string"},{"internalType":"address","name":"ReportCreatorAddress","type":"address"},{"internalType":"uint256","name":"avgRating","type":"uint256"},{"internalType":"uint256","name":"totalReviews","type":"uint256"},{"internalType":"address[]","name":"workers","type":"address[]"}],"internalType":"struct CrowdSource.Report","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getReportAvgRating","outputs":[{"internalType":"string","name":"rname","type":"string"},{"internalType":"uint256","name":"avgrating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReportsSubmittedByWorker","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tid","type":"uint256"}],"name":"getTask","outputs":[{"components":[{"internalType":"string","name":"taskTitle","type":"string"},{"internalType":"string","name":"taskDescription","type":"string"},{"internalType":"address","name":"taskCreatorAddress","type":"address"},{"internalType":"uint256","name":"minAmt","type":"uint256"}],"internalType":"struct CrowdSource.Task","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalTasks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"},{"internalType":"address","name":"worker","type":"address"}],"name":"getWorkerComments","outputs":[{"internalType":"string","name":"wComments","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"},{"internalType":"address","name":"worker","type":"address"}],"name":"getWorkerRating","outputs":[{"internalType":"uint256","name":"wRating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rIdSubmittedByWorkerAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wAddress","type":"address"},{"internalType":"uint256","name":"reportId","type":"uint256"},{"internalType":"uint256","name":"wRating","type":"uint256"},{"internalType":"string","name":"wComments","type":"string"}],"name":"reviewReport","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rid","type":"uint256"},{"indexed":false,"internalType":"string","name":"rname","type":"string"}],"name":"addReportEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tid","type":"uint256"},{"indexed":false,"internalType":"string","name":"tName","type":"string"}],"name":"addTaskEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"avgRating","type":"uint256"}],"name":"reviewReportEvent","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"ReportIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"TaskIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalRating","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalTasks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalwSubmittedReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wAddress","type":"address"},{"internalType":"string","name":"rname","type":"string"},{"internalType":"string","name":"_content","type":"string"}],"name":"addReport","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"rAddress","type":"address"},{"internalType":"string","name":"tName","type":"string"},{"internalType":"string","name":"tDescription","type":"string"},{"internalType":"uint256","name":"minAmtForTask","type":"uint256"}],"name":"addTask","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllReportIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllTaskIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getAllWorkersForReport","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getCurrentWorkerComments","outputs":[{"internalType":"string","name":"wComments","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getCurrentWorkerRating","outputs":[{"internalType":"uint256","name":"wRating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getReport","outputs":[{"components":[{"internalType":"string","name":"reportName","type":"string"},{"internalType":"string","name":"reportContent","type":"string"},{"internalType":"address","name":"ReportCreatorAddress","type":"address"},{"internalType":"uint256","name":"avgRating","type":"uint256"},{"internalType":"uint256","name":"totalReviews","type":"uint256"},{"internalType":"address[]","name":"workers","type":"address[]"}],"internalType":"struct CrowdSource.Report","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getReportAvgRating","outputs":[{"internalType":"string","name":"rname","type":"string"},{"internalType":"uint256","name":"avgrating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReportsSubmittedByWorker","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tid","type":"uint256"}],"name":"getTask","outputs":[{"components":[{"internalType":"string","name":"taskTitle","type":"string"},{"internalType":"string","name":"taskDescription","type":"string"},{"internalType":"address","name":"taskCreatorAddress","type":"address"},{"internalType":"uint256","name":"minAmt","type":"uint256"}],"internalType":"struct CrowdSource.Task","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalTasks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"},{"internalType":"address","name":"worker","type":"address"}],"name":"getWorkerComments","outputs":[{"internalType":"string","name":"wComments","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"},{"internalType":"address","name":"worker","type":"address"}],"name":"getWorkerRating","outputs":[{"internalType":"uint256","name":"wRating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rIdSubmittedByWorkerAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wAddress","type":"address"},{"internalType":"uint256","name":"reportId","type":"uint256"},{"internalType":"uint256","name":"wRating","type":"uint256"},{"internalType":"string","name":"wComments","type":"string"}],"name":"reviewReport","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3.toChecksumAddress('0x9d0260bff7ccE455325D5A524ad022f72E55772A')
contract  = web3.eth.contract(address=address, abi=abi)

# web3.eth.defaultAccount = web3.eth.accounts[0] 
# web3.eth.defaultAccount = input('Enter address: ')
# userAddress = web3.eth.defaultAccount

# print(web3.eth.defaultAccount)
# print(type(web3.eth.defaultAccount)) #string
workerData={'workerAddress':{},
            'reportIdsOfWorker':None,
            }

reportData={'reportId':None,
            'reportName':None,
            'reportContent':None,
            'reportAvgRating':None,
            'reportTotalReviews':None,
            'workersOfThisReport':None,
            'reportReviewData':{}
}


def createTask(walletAddress,taskName,taskDescription,taskAmount):
    # taskName = input('Enter Task Name: ')
    # taskDescription = input('Enter task Description: ')
    # taskAmount = int(input('Enter minimum amount for task: '))
    web3.eth.defaultAccount = walletAddress
    userAddress =web3.eth.defaultAccount
    tAmt= int(taskAmount)
    tx_hash = contract.functions.addTask(userAddress,taskName,taskDescription,tAmt).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    print('Task successfully created')


def getTask(tid):
    task= contract.functions.getTask(tid).call()
    print(task)
    return task

def getReportsCount(): #return integer
    numOfReports=contract.functions.getTotalReports().call()
    return numOfReports

def getAllReportIds(): #returns list
    report_ids= contract.functions.getAllReportIds().call()
    # print('reports IDs are',report_ids)
    return report_ids

def getReportAvgRating(report_id):
    reportRating = contract.functions.getReportAvgRating(report_id).call()
    # reviewData['reportRating'] = reportRating
    return reportRating 

def getCurrentWorkerComments(report_id):
    workerComments= contract.functions.getCurrentWorkerComments(report_id).call()
    # reviewData['reportComments'] = workerComments
    return workerComments

def getCurrentWorkerRating():
    report_id = input('Enter report_id: ')
    workerRatings = contract.functions.getCurrentWorkerRating(report_id).call()
    return workerRatings

def getAnyWorkerComments():
    worker_eth_address =  input('Enter eth address: ')
    report_id = input('Enter report_id: ')
    return contract.functions.getAnyWorkerComments(report_id, worker_eth_address).call()

def getAnyWorkerRating():
    worker_eth_address =  input('Enter eth address: ')
    report_id = input('Enter report_id: ')
    return contract.functions.getAnyWorkerRating(report_id, worker_eth_address).call()

def getAllWorkersForReport():
    report_id = input('Enter report_id: ')
    allWorkers = contract.functions.getAllWorkersForReport(report_id).call()
    return allWorkers

def getReportIdsByWorkerAddress():
    report_ids=contract.functions.getReportsSubmittedByWorker().call()
    return report_ids

def getWorkerCompleteData(wAddress):
    workerData['workerAddress']=wAddress
    rIdsOfWorker=getReportIdsByWorkerAddress()
    workerData['reportIdsOfWorker'] = rIdsOfWorker
    print(workerData)

def addReport(walletAddress,reportName,reportContent):
    web3.eth.defaultAccount = walletAddress
    userAddress =web3.eth.defaultAccount
    # reportName=input('Enter Report Name: ')
    # reportContent = input('Enter response for report: ')
    tx_hash = contract.functions.addReport(userAddress,reportName,reportContent).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    print('Report successfully added')
    print('New count of Reports: ', getReportsCount())

reviewData={'reportRating':None,
            'reportComments':None}

def getReport(rid):
    report=contract.functions.getReport(rid).call()
    rName,rContent,rWorkerAddress,rAvgRating,rTotalReviews,rSubmittedWorkers=report
    reviewData['reportRating'] = getReportAvgRating(rid)
    reviewData['reportComments'] = getCurrentWorkerComments(rid)
    reportData['reportId']=rid
    reportData['reportName']=rName
    reportData['reportContent']=rContent
    reportData['reportAvgRating']=rAvgRating
    reportData['reportTotalReviews']= rTotalReviews
    reportData['workersOfThisReport']= rSubmittedWorkers
    reportData['reportReviewData'] = reviewData
    print(reportData)
    return reportData


# addReport()
# getReportIdsByWorkerAddress()
# getTask(111)

def reviewReport(walletAddress,report_id,report_rating,report_feedback):
    web3.eth.defaultAccount = walletAddress
    userAddress =web3.eth.defaultAccount
    # report_id = int(input('Enter report_id: '))
    # print('Please review the report and rate it on scale of 1-5 and share feedback')
    # print(getReport(report_id))
    # report_rating = int(input('Enter rating: '))
    # report_feedback = input('Enter feedback: ')
    tx_hash = contract.functions.reviewReport(userAddress,report_id,report_rating,report_feedback).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    print('Successfully reviewed the report')

# # createTask()
# # addReport()
# reviewReport()


# print('-----User Data-----')
# getWorkerCompleteData(userAddress)

# print('-----Report Data-----')
# getReport(111112)
    


# addReport()
# getReportsCount()
# getAllReportIds()
# getReport()