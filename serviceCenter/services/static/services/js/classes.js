

function withDiscount(getPriceFunc, discount) {
    return function () {
        return getPriceFunc.call(this) * (1 - discount / 100);
    }
}

function Issue(device_type, issue_type, price) {
    this.device_type = device_type,
    this.issue_type = issue_type,
    this.price = price
}

Issue.prototype.getDeviceType = function () {
    return this.device_type;
};

Issue.prototype.setDeviceType = function (deviceType) {
    this.device_type = deviceType;
};

Issue.prototype.getIssueType = function () {
    return this.issue_type;
};

Issue.prototype.setIssueType = function (issue_type) {
    this.issue_type = issue_type;
};

Issue.prototype.getPrice = withDiscount(function () {
    return this.price;
}, 20);

Issue.prototype.setPrice = function (price) {
    this.price = price;
};

function AllIssue(destination, duration, price, count) {
    Issue.call(this, destination, duration, price);
    this.count = count;
}

AllIssue.prototype = Object.create(Issue.prototype);
AllIssue.prototype.constructor = AllIssue;

AllIssue.prototype.getCount = function () {
    return this.count;
};

AllIssue.prototype.setCount = function (count) {
    this.count = count;
};

/////////////////////////////
class Issue2 {
    constructor(device_type, issue_type, price) {
        this.device_type = device_type,
        this.issue_type = issue_type,
        this.price = price
    }

    get getDeviceType() {
        return this.device_type;
    }

    set setDeviceType(device_type) {
        this.device_type = device_type;
    }

    get getIssueType() {
        return this.issue_type;
    }

    set setIssueType(issue_type) {
        this.issue_type = issue_type;
    }

    get getPrice() {
        return this.price;
    }

    set setPrice(price) {
        this.price = price;
    }
}

class AllIssue2 extends Issue2 {
    constructor(destination, duration, price, count) {
        super(destination, duration, price);
        this.count = count;
    }

    get getCount() {
        return this.count;
    }

    set setCount(count) {
        this.count = count;
    }
}