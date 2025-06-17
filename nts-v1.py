import streamlit as st

# Set page configuration
st.set_page_config(page_title=".NET Tech Stack Explorer", layout="wide")

# Title and introduction
st.title("Explore the .NET Tech Stack")
st.markdown("""
The **.NET tech stack** is a powerful, cross-platform ecosystem by Microsoft for building modern applications across web, desktop, mobile, cloud, and more. 
This app provides an overview of its key components. Use the tabs below to dive into each category!
""")

# Create tabs for different .NET components
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Overview",
    "Web Development",
    "Desktop & Mobile",
    "Data Access",
    "Cloud & Microservices",
    "Game Development & AI",
    "Development Tools"
])

# Tab 1: Overview
with tab1:
    st.header("Overview of .NET")
    st.write("""
    .NET is a developer platform for building applications across platforms (Windows, macOS, Linux, iOS, Android). 
    Key features include:
    - **Unified Platform**: Combines .NET Framework and .NET Core into a single .NET (e.g., .NET 8, with .NET 9 expected in Nov 2025).
    - **Languages**: C# (primary), F#, VB.NET.
    - **Runtime**: Common Language Runtime (CLR) for execution, memory management, and security.
    - **Libraries**: Base Class Library (BCL) and NuGet packages for extensive functionality.
    """)
    st.info("Fun Fact: .NET supports everything from web APIs to games in Unity!")

# Tab 2: Web Development
with tab2:
    st.header("Web Development with .NET")
    st.write("""
    **ASP.NET Core** is the flagship framework for web development in .NET, offering:
    - **MVC**: Structured web apps with Model-View-Controller pattern.
    - **Razor Pages**: Simplified page-based web development.
    - **Blazor**: Interactive UIs using C# (Server or WebAssembly).
    - **Web API**: RESTful APIs for modern applications.
    - **SignalR**: Real-time features (e.g., chat, live updates).
    - **Minimal APIs**: Lightweight API development (introduced in .NET 6).
    - **gRPC**: High-performance RPC services.
    """)
    st.code("""
    // Example: Minimal API in ASP.NET Core
    var app = WebApplication.Create();
    app.MapGet("/", () => "Hello, .NET Web!");
    app.Run();
    """, language="csharp")
    st.success("ASP.NET Core powers fast, scalable web apps with cross-platform support.")

# Tab 3: Desktop & Mobile
with tab3:
    st.header("Desktop and Mobile Development")
    st.write("""
    .NET supports desktop and mobile apps with:
    - **Windows Forms**: Traditional Windows desktop apps (legacy).
    - **WPF**: Modern Windows apps with XAML-based UI.
    - **.NET MAUI**: Cross-platform apps for Windows, macOS, iOS, and Android.
    - **Xamarin**: Legacy framework for mobile apps (replaced by MAUI).
    """)
    st.code("""
    // Example: .NET MAUI Button Click Handler
    <Button Text="Click Me" Clicked="OnButtonClicked" />
    
    private void OnButtonClicked(object sender, EventArgs e)
    {
        DisplayAlert("Hello", "Welcome to .NET MAUI!", "OK");
    }
    """, language="csharp")
    st.info(".NET MAUI lets you write one codebase for multiple platforms!")

# Tab 4: Data Access
with tab4:
    st.header("Data Access in .NET")
    st.write("""
    .NET provides robust data access tools:
    - **Entity Framework Core (EF Core)**: Lightweight ORM for SQL Server, PostgreSQL, SQLite, etc.
    - **ADO.NET**: Low-level database access for high performance.
    - **Dapper**: Fast, lightweight micro-ORM.
    """)
    st.code("""
    // Example: EF Core Query
    using var context = new MyDbContext();
    var users = await context.Users.Where(u => u.Age > 18).ToListAsync();
    """, language="csharp")
    st.success("EF Core simplifies database interactions with LINQ queries.")

# Tab 5: Cloud & Microservices
with tab5:
    st.header("Cloud and Microservices")
    st.write("""
    .NET is optimized for cloud and microservices:
    - **Azure Integration**: Seamless with Azure Functions, App Services, and AKS.
    - **Docker**: Built-in container support.
    - **Microservices**: Tools like ASP.NET Core, gRPC, Polly, and Dapr.
    """)
    st.code("""
    // Example: Azure Function in .NET
    public static class HelloFunction
    {
        [FunctionName("HelloFunction")]
        public static IActionResult Run([HttpTrigger] HttpRequest req)
        {
            return new OkObjectResult("Hello from Azure!");
        }
    }
    """, language="csharp")
    st.info("Deploy .NET apps to Azure for scalable cloud solutions.")

# Tab 6: Game Development & AI
with tab6:
    st.header("Game Development and AI")
    st.write("""
    - **Unity**: Uses C# and .NET for game scripting.
    - **MonoGame**: Cross-platform game framework.
    - **ML.NET**: Machine learning framework for .NET.
    - **ONNX Runtime**: Run pre-trained ML models.
    """)
    st.code("""
    // Example: Unity C# Script
    public class Player : MonoBehaviour
    {
        void Update()
        {
            if (Input.GetKeyDown(KeyCode.Space))
                Debug.Log("Jump!");
        }
    }
    """, language="csharp")
    st.success("Unity and ML.NET extend .NET to gaming and AI.")

# Tab 7: Development Tools
with tab7:
    st.header("Development Tools")
    st.write("""
    .NET offers powerful tools:
    - **Visual Studio**: Premier IDE for .NET development.
    - **VS Code**: Lightweight editor with C# extensions.
    - **Rider**: JetBrains' cross-platform IDE.
    - **.NET CLI**: Command-line tool for building, testing, and publishing.
    - **Roslyn**: Compiler platform for code analysis.
    """)
    st.code("""
    # Example: .NET CLI to create a new project
    dotnet new webapi -o MyApi
    cd MyApi
    dotnet run
    """, language="bash")
    st.info("Visual Studio provides a rich environment for .NET developers.")

# Sidebar for additional info
with st.sidebar:
    st.header("About .NET")
    st.write("""
    .NET is maintained by Microsoft and supports high-performance, cross-platform development.
    - Latest Version: .NET 8 (as of June 2025)
    - Next Release: .NET 9 (expected Nov 2025)
    - Learn more at [dotnet.microsoft.com](https://dotnet.microsoft.com)
    """)
    st.image("https://dotnet.microsoft.com/static/images/redesign/shared/dotnet-logo.svg", width=150)

# Footer
st.markdown("---")
st.write("Built with Streamlit | Data sourced from .NET documentation | © 2025")
