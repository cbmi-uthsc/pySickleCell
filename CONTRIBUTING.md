CBMI@UTHSC Contibution Guidelines
Before submitting a feature or substantial code contribution please discuss it with the team and ensure it follows the product roadmap. The team rigorously reviews and tests all code submissions. The submissions must meet an extremely high bar for quality, design, and roadmap appropriateness.
Contributors should ensure they follow these guidelines when making submissions.

For now, the team has set the following limits on pull requests:

    Contributions beyond the level of a bug fix must be discussed with the team first, or they will likely be declined. As our process matures and our experience grows, the team expects to take larger contributions.
    Pull requests that do not merge easily with the tip of the master branch will be declined. The author will be asked to merge with tip and update the pull request.
    Submissions must meet functional and performance expectations, including scenarios for which the team doesn’t yet have open source tests. This means you may be asked to fix and resubmit your pull request against a new open test case if it fails one of these tests.
When you are ready to proceed with making a change, get set up to build the code and familiarize yourself with our workflow and our coding conventions

Developer Workflow
When the pull request process deems the change ready it will be merged directly into the tree.



Creating New Issues

Please follow these guidelines when creating new issues in the issue tracker:

    Use a descriptive title that identifies the issue to be addressed or the requested feature. For example when describing an issue where the compiler is not behaving as expected, write your bug title in terms of what the compiler should do rather than what it is doing – “Python 3 compiler should report CS2654 when abcd is used in xyz.”
    Do not set any bug fields other than Impact.
    Specify a detailed description of the issue or requested feature.
    For bug reports, please also:
        Describe the expected behavior and the actual behavior. If it is not self-evident such as in the case of a crash, provide an explanation for why the expected behavior is expected.
        Provide example code that reproduces the issue.
        Specify any relevant exception messages and stack traces.
    Subscribe to notifications for the created issue in case there are any follow up questions.

Coding Conventions

    
    Use plain code to validate parameters at public boundaries. Do not use Contracts or magic helpers.

if (argument == null):
	
	do_something()

    
Code Formatter: Coming soon..


Python Conventions:

For all of the Python 3 guidelines which have analogs in Python 3, the team applies the spirit of the guideline to Python 3. Guidelines surrounding spacing, indentation, parameter names, and the use of named parameters are all generally applicable to Python 3. ‘Dim’ statements should also follow the guidelines for the use of ‘var’ in Python 3. Specific to Python 3, field names should begin with ‘m_’ or ‘_’. And the team prefers that all field declarations be placed at the beginning of a type definition
Tips 'n' Tricks:Coming soon
