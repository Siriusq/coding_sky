const consoleLogList = document.querySelector('.editor__console-logs');
const executeCodeBtn = document.querySelector('.editor__run');
const resetCodeBtn = document.querySelector('.editor__reset');

let defaultCode = '//IDE\nconsole.log("Hello World!")';
let consoleMessages = [];

var editor0 = ace.edit('code');
    editor0.setTheme("ace/theme/dracula");
    editor0.session.setMode("ace/mode/javascript");
    editor0.setFontSize(18);
    editor0.setOptions({
        enableBasicAutocompletion: true,
        enableLiveAutocompletion: true,
    });
    editor0.resize();

let consoleManager = {
    clearConsoleScreen(){
        consoleMessages.length = 0;
        while(consoleLogList.firstChild){
            consoleLogList.removeChild(consoleLogList.firstChild);
        }
    },

    printToConsole(){
        consoleMessages.forEach(log => {
            const newLogItem = document.createElement('li');
            const newLogText = document.createElement('pre');

            newLogText.className = log.class;
            newLogText.textContent = `> ${log.message}`;

            newLogItem.appendChild(newLogText);

            consoleLogList.appendChild(newLogItem);
        })
    },
}



var editor1 = ace.edit('code1');
    editor1.setTheme("ace/theme/dracula");
    editor1.session.setMode("ace/mode/javascript");
    editor1.setReadOnly(true);
    editor1.setFontSize(18);
    editor1.resize();

var editor2 = ace.edit('code2');
    editor2.setTheme("ace/theme/dracula");
    editor2.session.setMode("ace/mode/javascript");
    editor2.setReadOnly(true);
    editor2.setFontSize(18);
    editor2.resize();

var editor3 = ace.edit('code3');
    editor3.setTheme("ace/theme/dracula");
    editor3.session.setMode("ace/mode/javascript");
    editor3.setReadOnly(true);
    editor3.setFontSize(18);
    editor3.resize();

var editor4 = ace.edit('code4');
    editor4.setTheme("ace/theme/dracula");
    editor4.session.setMode("ace/mode/javascript");
    editor4.setReadOnly(true);
    editor4.setFontSize(18);
    editor4.resize();

var editor5 = ace.edit('code5');
    editor5.setTheme("ace/theme/dracula");
    editor5.session.setMode("ace/mode/javascript");
    editor5.setReadOnly(true);
    editor5.setFontSize(18);
    editor5.resize();

var editor6 = ace.edit('code6');
    editor6.setTheme("ace/theme/dracula");
    editor6.session.setMode("ace/mode/javascript");
    editor6.setReadOnly(true);
    editor6.setFontSize(18);
    editor6.resize();

var editor7 = ace.edit('code7');
    editor7.setTheme("ace/theme/dracula");
    editor7.session.setMode("ace/mode/javascript");
    editor7.setReadOnly(true);
    editor7.setFontSize(18);
    editor7.resize();

var editor8 = ace.edit('code8');
    editor8.setTheme("ace/theme/dracula");
    editor8.session.setMode("ace/mode/javascript");
    editor8.setReadOnly(true);
    editor8.setFontSize(18);
    editor8.resize();

var editor9 = ace.edit('code9');
    editor9.setTheme("ace/theme/dracula");
    editor9.session.setMode("ace/mode/javascript");
    editor9.setReadOnly(true);
    editor9.setFontSize(18);
    editor9.resize();

// Events
executeCodeBtn.addEventListener('click', () => {
    // Clear console messages
    consoleManager.clearConsoleScreen();
    
    // Get input from the code editor
    const userCode = editor0.getValue();

    // Run the user code
    try {
        new Function(userCode)();
    } catch (err) {
        console.error(err);
    }

    // Print to the console
    consoleManager.printToConsole();
});

resetCodeBtn.addEventListener('click', () => {
    // Clear ace editor
    editor0.setValue(defaultCode);

    // Clear console messages
    consoleManager.clearConsoleScreen();
})

let console = (function (oldConsole) {
    return {
        formatArgsOutput: function(arg) { 
            let outputArgMessage;

            // Deal with different data types
            switch (this.getType(arg)) {
                case "string":
                    outputArgMessage = `"${arg}"`;
                    break;
                case "object":
                    outputArgMessage = `Object ${JSON.stringify(arg)}`;
                    break;
                case "array":
                    outputArgMessage = `Array ${JSON.stringify(arg)}`;
                    break;
                default:
                    outputArgMessage = arg;
                    break;
            }

            return outputArgMessage;
        },
        getType: function (arg) {
            if (typeof arg === "string") return "string";
            if (typeof arg === "boolean") return "boolean";
            if (typeof arg === "function") return "function";
            if (typeof arg === "number") return "number";
            if (typeof arg === "undefined") return "undefined";
            if (typeof arg === "object" && !Array.isArray(arg)) return "object";
            if (typeof arg === "object" && Array.isArray(arg)) return "array";
        },
        logMultipleArguments: function (arguments) {
            let currentLog = "";

            // Deal with multiple arguments
            arguments.forEach(arg => {
                currentLog += this.formatArgsOutput(arg) + " ";
            });

            oldConsole.log.apply(oldConsole, arguments);

            consoleMessages.push({
                message: currentLog,
                class: `log log--default`
            });

            oldConsole.log(consoleMessages);
        },
        logSingleArgument: function (logItem) {
            oldConsole.log(logItem);
            consoleMessages.push({
                message: this.formatArgsOutput(logItem),
                class: `log log--${this.getType(logItem)}`
            });

            oldConsole.log(consoleMessages);
        },
        log: function (text) {
            let argsArray = Array.from(arguments);
            return argsArray.length !== 1 ? this.logMultipleArguments(argsArray) : this.logSingleArgument(text);
        },
        info: function (text) {
            oldConsole.info(text);
        },
        warn: function (text) {
            oldConsole.warn(text);
        },
        error: function (err) {
            oldConsole.error(err);
            consoleMessages.push({
                message: `${err.name}: ${err.message}`,
                class: "log log--error"
            });
        }
    }
})(window.console);